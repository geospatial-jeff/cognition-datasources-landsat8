from datasources import Manifest

def Landsat8(event, context):
    manifest = Manifest()
    manifest['Landsat8'].search(**event)
    response = manifest.execute()
    return response


