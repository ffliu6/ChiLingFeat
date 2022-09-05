import extractor

text = '我爱去天安门广场。你觉得怎么样呢？今天我们还去吗？'

LingFeat = extractor.pass_text(text)

# LingFeat.preprocess(short=True, see_token=True, see_sent_token=True)
# print(LingFeat.preprocess(short=True, see_token=True, see_sent_token=True))

LingFeat.preprocess(short=True)

all = []
ShaF = LingFeat.ShaF_() # 35
print('ShaF success')
PosF = LingFeat.POSF_()
print('PosF success')
PhrF = LingFeat.PhrF_()
print('PhrF success')
TrsF = LingFeat.TrSF_()
print('TrsF success')
EndF = LingFeat.EnDF_()
print('EndF success')
EngF = LingFeat.EnGF_()
print('EngF success')
VarF = LingFeat.VarF_()
print('VarF success')
TtrF = LingFeat.TTRF_()
print('TtrF success')

all.extend(ShaF)
all.extend(PhrF)
all.extend(TrsF)
all.extend(EndF)
all.extend(EngF)
all.extend(VarF)
all.extend(TrsF)
all.extend(PosF)
print(len(all))