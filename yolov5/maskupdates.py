import requests
import mindsphere as ms
import json

class PCData(object):
    
    def __init__(self):
        self.pc = ms.PCInformation()
        self.mask = self.pc.mask()
        self.stop = False
    
    def getPayloadData(self):
        return self.createPayload(People_mask=self.mask)

    @classmethod
    def createPayload(self, People_mask, c8y_key='c8y_Mask_people', fragment_name='M'):
        payload = {}
        fragment_data = {}
        value = {}
        value["value"] = People_mask
        value["unit"]  = 'M'
        fragment_data[fragment_name] = value
        payload[c8y_key] = fragment_data
        return payload

if __name__ == "__main__":
    PC = PCData()
    PC.getPayloadData()


