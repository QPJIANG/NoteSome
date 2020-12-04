



```javascript
if (document.getElementById("iframe-main")) {
  document.getElementById("iframe-main").src = url;
} else {
  var iframe = document.createElement("iframe");
  var container = document.getElementById("content-main");

  iframe.style.width = "100%";
  iframe.id = "iframe-main";
  iframe.style.height = "650px";
  // iframe.style.margin = '0';
  // iframe.style.padding = '0';
  iframe.scrolling = "no";
  iframe.frameBorder = "no";
  if (iframe.attachEvent) {
    iframe.attachEvent("onload", function () {
      ......
    });
  } else {
    iframe.onload = function () {
      .....
    };
  }
  iframe.src = url;
  container.appendChild(iframe);
}

```

