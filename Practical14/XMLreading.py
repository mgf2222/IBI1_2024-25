import os
import xml.dom.minidom as minidom
import xml.sax
from datetime import datetime

# Set working directory
os.chdir('Practical14')
#If the file cannot be read correctly, use the absolute path below
#os.chdir(r"D:\IBI\IBImidterm\IBI1_2024-25\Practical14")

# ======================== DOM Parsing ========================
def dom_analysis():
    start_time = datetime.now()  # Start timing
    
    # Initialize result storage structure
    max_counts = {
        'molecular_function': {'ids': [], 'count': 0},
        'biological_process': {'ids': [], 'count': 0},
        'cellular_component': {'ids': [], 'count': 0}
    }
    
    # Parse XML document
    dom = minidom.parse('go_obo.xml')
    terms = dom.getElementsByTagName('term')
    
    for term in terms:
        # Extract namespace and is_a count
        namespace_nodes = term.getElementsByTagName('namespace')
        if not namespace_nodes:
            continue
        namespace = namespace_nodes[0].firstChild.data.strip()
        
        if namespace not in max_counts:
            continue
        
        is_a_count = len(term.getElementsByTagName('is_a'))
        id_node = term.getElementsByTagName('id')[0].firstChild.data.strip()
        
        # Update maximum count record
        current = max_counts[namespace]
        if is_a_count > current['count']:
            current['count'] = is_a_count
            current['ids'] = [id_node]
        elif is_a_count == current['count']:
            current['ids'].append(id_node)
    
    # Output results
    print("DOM Results:")
    for ontology, data in max_counts.items():
        print(f"{ontology}: {data['ids']} with {data['count']} is_a elements")
    
    return datetime.now() - start_time  # Return parsing duration

# ======================== SAX Parsing ========================
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.max_counts = {
            'molecular_function': {'ids': [], 'count': 0},
            'biological_process': {'ids': [], 'count': 0},
            'cellular_component': {'ids': [], 'count': 0}
        }
        self.current_id = ""
        self.current_namespace = ""
        self.is_a_count = 0
        self.in_id = False
        self.in_namespace = False

    def startElement(self, tag, _):
        # Handle start of XML elements
        if tag == 'term':
            self.current_id = ""
            self.current_namespace = ""
            self.is_a_count = 0
        elif tag == 'id':
            self.in_id = True
        elif tag == 'namespace':
            self.in_namespace = True
        elif tag == 'is_a':
            self.is_a_count += 1

    def characters(self, content):
        # Handle text content within elements
        if self.in_id:
            self.current_id += content.strip()
        elif self.in_namespace:
            self.current_namespace += content.strip()

    def endElement(self, tag):
        # Handle end of XML elements
        if tag == 'term':
            if self.current_namespace in self.max_counts:
                current = self.max_counts[self.current_namespace]
                if self.is_a_count > current['count']:
                    current['count'] = self.is_a_count
                    current['ids'] = [self.current_id]
                elif self.is_a_count == current['count']:
                    current['ids'].append(self.current_id)
        elif tag == 'id':
            self.in_id = False
        elif tag == 'namespace':
            self.in_namespace = False

def sax_analysis():
    start_time = datetime.now()  # Start timing
    parser = xml.sax.make_parser()
    handler = GOHandler()
    parser.setContentHandler(handler)
    parser.parse('go_obo.xml')
    
    print("\nSAX Results:")
    for ontology, data in handler.max_counts.items():
        print(f"{ontology}: {data['ids']} with {data['count']} is_a elements")
    
    return datetime.now() - start_time  # Return parsing duration

# ======================== Main Program ========================
if __name__ == "__main__":
    # Execute parsing and time measurement
    dom_duration = dom_analysis()
    sax_duration = sax_analysis()
    
    # Output time comparison
    print(f"\nDOM Time: {dom_duration.total_seconds():.2f}s")
    print(f"SAX Time: {sax_duration.total_seconds():.2f}s")
    # SAX parsing is typically faster as it doesn't load the entire document into memory
    if dom_duration < sax_duration:
        print("\nDOM parsing is faster.")
    elif dom_duration > sax_duration:
        print("\nSAX parsing is faster.")
    else:
        print("\nBoth parsing methods have the same execution time.")