let nav_h = document.querySelector('.navbar').clientHeight;
let con_h = document.querySelector('div.contents').clientHeight;
let footer_h = document.querySelector('footer').clientHeight;

//  navbar, container(contents) , footer 높이 콘솔 출력
console.log(nav_h, con_h, footer_h)
// viewport 높이
console.log(window.innerHeight)
// html 콘텐츠 문서의 높이
doc_g = nav_h + con_h + footer_h
// 높이의 따른 fixed-bottom 처리

if( doc_g >= window.innerHeight ){

    document.querySelector('footer').classList.remove('fixed-bottom')
}
