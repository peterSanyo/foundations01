const myImage = document.querySelector("img");

myImage.onclick = () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "images/01_gallery.jpg") {
    myImage.setAttribute("src", "images/furniture.jpg");
  } else {
    myImage.setAttribute("src", "images/01_gallery.jpg");
  }
};
