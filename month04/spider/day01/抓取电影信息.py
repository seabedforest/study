import re
html="""<div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1375" title="活着" data-act="boarditem-click" data-val="{movieId:1375}">活着</a></p>
        <p class="star">
                主演：葛优,巩俐,牛犇（bēn）
        </p>
<p class="releasetime">上映时间：1994-05-17(法国)</p>    </div>"""
regex='<div class="board-item-content">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
pattern=re.compile(regex,re.S)
result=pattern.findall(html)
print(result)