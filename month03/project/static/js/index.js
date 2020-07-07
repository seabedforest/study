var BASE_URL='../static/images/';  //规定当前文件中的图片的地址
// 轮播图
$(function(){
    // alert('外部JS加载完成');
    // console.log(faderData);
    // console.log(blogData);
    
    // 根据从faderData中获取的数据拼接字符串
    var html='';
    $.each(faderData,function(i,obj){
        html +='<li class="slide">';
        html +='<a href="#">';
        html +=`<img src="${BASE_URL+obj.img_url}" alt=""></a>`;
        html +=`<div class="imginfo">${obj.img_info}</div></li>`;
    })
    html+='<li class="fader_controls">';
    html +='<div class="page prev" data-target="prev">&lsaquo;</div>';
    html+='<div class="page next" data-target="next">&rsaquo;</div>';
    html+='<ul class="pager_list">';
    html+='</ul></li>'
    // easyFader()是由easyfader.min.js提供的功能  实现图片轮播效果
    $("#fader").html(html).easyFader({
        slideDur:4000,  //切换图片的时间间隔 ms
        fadeDur:1000,   //过渡的事件 ms
    });
})

// 博客
$(function(){
    // console.log(blogData);
    // // arr.slice(start,end) 截取数组  从指定索引值start开始到end结束 不包含end
    var data = blogData.slice(0,4);
    // console.log(data);
    function add_blogs(data){
        $.each(data,function(i,obj){
            $(".blogsbox").append(`<div class="blogs">
            <h3 class="blogtitle">
                <a href="#">${obj.blogtitle}</a>
            </h3>
            <span class="blogpic">
                <a href="#"><img src="../static/images/${obj.blogpic}" alt=""></a>
            </span>
            <p class="blogtext">${obj.blogtext}</p>
            <ul class="bloginfo">
                <li class="author"><a href="#">${obj.bloginfo.author}</a></li>
                <li class="lnname"><a href="#">${obj.bloginfo.lmname}</a></li>
                <li class="timer"><a href="#">${obj.bloginfo.timer}</a></li>
                <li class="view"><a href="#">${obj.bloginfo.view}</a></li>
                <li class="like"><a href="#">${obj.bloginfo.like}</a></li>
            </ul>
        </div>`)
        })
    }
    add_blogs(data);

    var canLoad = true;  //能否加载数据  默认可以加载
    // 滚动条滚动事件
    $(document).scroll(function(){
        // console.log('滚');
        // 获取滚动条高度
        var scrollTop=Math.round($(document).scrollTop());
        // 获取可视范围高度
        var windowHeight=$(window).height();
        // 获取完整文档高度
        var documentHeight=$(document).height();
        // console.log(scrollTop,windowHeight,documentHeight);
        if(documentHeight-(scrollTop+windowHeight) <=150){
            if(canLoad){
                var i = $('.blogs').length;
                var data =blogData.slice(i,i+5);
                if(data.length>0){
                    add_blogs(data);
                }else{
                    if(documentHeight==scrollTop+windowHeight){
                        alert('我是有底线的')
                        canLoad=false;
                    }
                }

            }
        }
    })
})