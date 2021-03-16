var randomno = Math.floor(Math.random()*6) + 1;

var randomdice = "dice"+ randomno +".png";

var randimg= "images/"+ randomdice;

   document.querySelectorAll("img")[0].setAttribute("src", randimg);
   var randomno1 = Math.floor(Math.random()*6) + 1;

   var randomdice1 = "dice"+ randomno1 +".png";
   var randimg1= "images/"+ randomdice1;
    document.querySelectorAll("img")[1].setAttribute("src", randimg1);
if(randomno>randomno1)
document.querySelector("h2").innerHTML="🚩player 1 wins!!!"
else if(randomno<randomno1)
document.querySelector("h2").innerHTML="🚩player 2 wins!!!"
else
document.querySelector("h2").innerHTML="match draw!!!"
