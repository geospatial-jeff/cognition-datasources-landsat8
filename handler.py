from datasources import Manifest

def handler(event, context):
    m = Manifest()
    print(list(m.sources))

