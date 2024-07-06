import lxml.etree as etree

# namespace 
namespaces = {
    'akn': 'http://docs.oasis-open.org/legaldocml/ns/akn/3.0/CSD11',
    'nrdfa': 'http://www.normattiva.it/rdfa/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'eli': 'http://data.europa.eu/eli/ontology#',
    'nakn': 'http://docs.oasis-open.org/legaldocml/ns/akn/3.0/N-AKN-NS#'
}

tree = etree.parse("C:\\Users\\erica\\Desktop\\palmy\\20200317_20G00034_VIGENZA_20240327.xml")
root = tree.getroot()

document_uri = root.xpath('//akn:FRBRuri/@value', namespaces=namespaces)
document_pub_num = root.xpath('//akn:publication/@number', namespaces=namespaces)
dates_of_modification = root.xpath('//akn:eventRef/@date', namespaces=namespaces)
sources_of_modification = root.xpath('//akn:eventRef/@source', namespaces=namespaces)
eli_title_contents = root.xpath('//nrdfa:span[@property="eli:title"]/@content', namespaces=namespaces)


# Stack to delete duplicates
stack = set(document_uri)


print("\nDocument title:")
for content in eli_title_contents:
    print(content)


print("\nDocument URI:")
for uri in stack:
    print(uri)


print("\nPublication number:")
for num in document_pub_num:
    print(num)

print("\nAmendment regulation dates:")
for i in range(len(dates_of_modification)):
    date = dates_of_modification[i]
    source = sources_of_modification[i] if i < len(sources_of_modification) else ""
    print(f"Date: {date}, Source: {source}")




