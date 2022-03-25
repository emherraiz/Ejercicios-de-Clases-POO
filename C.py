class A:
    def z(self):
        return self

    def y(self, t):
        return len(t)

a = A

y = a.z

print(y(a))
aa = a()
print(aa is a())
z = aa.y
print(z(()))
print(a().y((a,)))
print(A.y(aa, (a,z)))
print(aa.y((z,1,'z')))

print(f'\nA = {A}')
print(f'a = {a}')
print(f'y = {y}')
print(f'aa = {aa}')
print(f'z = {z}')

