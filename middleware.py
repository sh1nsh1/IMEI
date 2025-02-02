async def validate_imei(imei:str):
    return imei.isdigit() and ( len(imei) == 15)
