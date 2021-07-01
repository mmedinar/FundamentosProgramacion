
versiones = dict(python=2.7, zope = 2.13, plone=5.1)
print(versiones)

#GET
print(versiones.get('zope'))
print(versiones.get('loco','el valor no se encontro'))


#DELETE
del versiones['python']
print(versiones)

print(versiones.pop('zope'))
print(versiones)


#UPDATES
print('ejemplo update')
versiones = dict(python=2.7, zope = 2.13, plone=5.1)
print(versiones)
versiones_adicional = dict(django=2.1)
print(versiones_adicional)
print(versiones.update(versiones_adicional))
