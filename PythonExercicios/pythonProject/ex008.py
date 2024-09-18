m = float(input('Digite uma medida em metros '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('O valor da medida é {}km \n O valor da medida é {}hm \n O valor da medida é {}dam \n O valor da medida é {}m \n O valor da medida é {:.0f}dm \n O valor da medida é {:.0f}cm \n O valor da medida é {:.0f}mm'.format(km, hm, dam, m, dm, cm, mm))
