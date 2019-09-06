# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = float(input())
bc = float(input())
ac = (ab ** 2 + bc ** 2) ** 0.5
#print(ac)
acb = math.atan(ab / bc)
#print(math.degrees(acb))
mb = (bc ** 2 + (ac / 2) ** 2 - 2 * bc * (ac / 2) * math.cos(acb)) ** 0.5
print('%d°' % (round(math.degrees(math.acos(mb * math.cos(acb) / (ac / 2))))))
