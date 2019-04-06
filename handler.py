from datasources import Manifest

def Landsat8(event, context):
    manifest = Manifest()
    manifest['Landsat8'].search(event['spatial'], event['temporal'], event['properties'], **event['kwargs'])
    response = manifest.execute()
    return response


