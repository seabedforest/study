import re

html = """
<div class="animal">
    <p class="name">
			<a title="Tiger"></a>
    </p>
    <p class="content">
			Two tigers two tigers run fast
    </p>
</div>
<div class="animal">
    <p class="name">
			<a title="Rabbit"></a>
    </p>
    <p class="content">
			Small white rabbit white and white
    </p>
</div>
"""
pattern = re.compile('<div class="animal">.*?<a title="(.*?)".*?<p class="content">(.*?)</p>.*?</div>', re.S)
result = pattern.findall(html)
for rt in result:
    print('动物名称:', rt[0].strip())
    print('动物描述:', rt[1].strip())
    print('*' * 50)
