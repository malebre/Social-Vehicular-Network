from xml.dom.minidom import * 

def modify_node(node,value):
    for n in node.childNodes:
        if n.nodeType == Node.ELEMENT_NODE:
		if n.nodeName=="scale":
			n.setAttribute("value", value)
        modify_node(n,value) 

def changeValueDensity(File,value):

	try:
		xmldoc=parse(File)
		node_racine=xmldoc.documentElement
		modify_node(node_racine,value)
		filexsl = open(File,"w")
		filexsl.write(xmldoc.toxml())
		filexsl.close()
	except Exception, e:
    		raise e
