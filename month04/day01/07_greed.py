import re

html = """
<div><p>如果你为门中弟子伤她一分，我便屠你满门</p></div>
<div><p>如果你为为天下人损她一毫，我便杀尽天下人</p></div>
"""

pattern = re.compile('<div><p>(.*?)</p></div>', re.S)
rlist=pattern.findall(html)
print(rlist)