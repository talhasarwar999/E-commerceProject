
function setCookie(cname, cvalue) {
  const d = new Date();
  d.setTime(d.getTime() + (3 * 24 * 60 * 60 * 1000));
  let expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  let name = cname + "=";
  let ca = document.cookie.split(';');
  for(let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
}

return "";
}

function deleteCookie( name, path, domain ) {
  if( getCookie( name ) ) {
    document.cookie = name + "=" +
      ((path) ? ";path="+path:"")+
      ((domain)?";domain="+domain:"") +
      ";expires=Thu, 01 Jan 1970 00:00:01 GMT";
  }
}

function getCartCount(){
  let productsCount = 0;
  let products = document.cookie.split(';').reduce((ac, str) => Object.assign(ac, {[str.split('=')[0].trim()]: str.split('=')[1]}), {});
  Object.keys(products).forEach(item => {
    let temp = item.split('-');
    if(temp[0] == 'product') productsCount++;
  })
  return productsCount;
}