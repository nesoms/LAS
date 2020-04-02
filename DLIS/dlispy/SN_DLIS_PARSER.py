from dlispy import LogicalFile, Object, Attribute, FrameData, PrivateEncryptedEFLR, parse
# you can also set eflrOnly as True to only load EFLRs
_, logical_file_list = parse('../data/206_05a-_3_DWL_DWL_WIRE_258276498.DLIS', eflr_only= False)
for lf  in logical_file_list: # type:LogicalFile
    print("LogicalFile with ID:{}, SequenceNumber:{}".format(lf.id, lf.seqNum))
    for eflr in lf.eflrList:
        if type(eflr) is PrivateEncryptedEFLR:              # PrivateEncryptedEFLR needs to handle separately.
            continue
        print("     Set with Type:{}, Name:{}".format(eflr.setType, eflr.setName))
        for obj in eflr.objects: # type:Object
            print("             Object with Name:{}".format(obj.name))
            for attribute in obj.attributes:    #type:Attribute
                print("                     Attribute with Label:{}, Value:{}, Count:{}, RepCode:{}, Units:{} ".
                      format(attribute.label, ' '.join(map(str, attribute.value))
                      if type(attribute.value) is list else attribute.value,
                      attribute.count, attribute.repCode, attribute.units))

    for frameName, fDataList in lf.frameDataDict.items():
        print("     Frame:{}".format(frameName))
        for fdata in fDataList: # type:FrameData
            print("             FrameData with FrameNumber:{} and {} of slots".
            format(fdata.frameNumber, len(fdata.slots)))