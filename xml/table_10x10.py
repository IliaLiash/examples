print('<html><body><table>')
s1 = 10
for i in range(1, s1+1):
     print('<tr><td>',*range(i, i*s1+1, i), sep='\t',end='</td></tr>\n')
print('</table></body></html>')