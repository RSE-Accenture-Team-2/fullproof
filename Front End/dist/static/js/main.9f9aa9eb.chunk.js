(this.webpackJsonpkanye=this.webpackJsonpkanye||[]).push([[0],{37:function(e,t,a){},58:function(e,t,a){e.exports=a(72)},72:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),l=a(9),o=a.n(l),i=(a(37),a(12)),c=a(13),s=a(16),u=a(14),m=a(25),h=a(92),d=a(15),g=a(20),f=a(93),p=a(87),v=a(88),b=a(90),E=a(94),w=a(55),j=a(24),O=a(3),k=a.n(O),y=Object(n.forwardRef)((function(e,t){var a=e.children,n=e.isDragActive,l=e.files,o=Object(j.a)(e,["children","isDragActive","files"]);return r.a.createElement(f.a,Object.assign({background:(n||l.length,"white"),border:{color:n?"brand":"light-5",style:"dashed",size:"small"},height:{min:"small"},align:l.length?"stretch":"center",justify:"center",pad:"xsmall",ref:t},o),a)}));y.propTypes={isDragActive:k.a.bool.isRequired,files:k.a.array.isRequired,children:k.a.node.isRequired};var x=a(97),S=a(95),D=function(e){var t=e.multiple;return r.a.createElement(x.a,null,"Drag and drop or ",r.a.createElement(S.a,null,"choose")," ",t?"files":"a file")},F=function(e){var t=e.multiple;return r.a.createElement(x.a,{color:"brand",weight:"bold"},"Drop ",t?"files":"file"," here")},C=a(91),z=function(e){var t=e.file,a=e.removeFile,n=e.showPreview,l=e.showFileSize,o=Object(j.a)(e,["file","removeFile","showPreview","showFileSize"]);return r.a.createElement(f.a,Object.assign({direction:"row",align:"center",justify:"between"},o),r.a.createElement(I,{file:t,showFileSize:l,showPreview:n}),r.a.createElement(T,{file:t,removeFile:a}))},T=function(e){var t=e.file,a=e.removeFile;return r.a.createElement(E.a,{a11yTitle:"remove ".concat(t.path),icon:r.a.createElement(C.a,null),hoverIndicator:!0,onClick:function(){return a(t)}})};z.defaultProps={showPreview:!1,showFileSize:!1};var N=a(96),P="bytes",R="KB",B="MB",L="GB",A=function(e){for(var t=e,a=0;t>1e3;)t/=1e3,a+=1;return{value:t,suffix:0===a?P:1===a?R:2===a?B:L}};var I=function(e){var t,a=e.file,n=e.showPreview,l=e.showFileSize;return r.a.createElement(f.a,{direction:"row",gap:"xsmall",align:"center"},n&&r.a.createElement(f.a,{width:"xxsmall",height:"xxsmall"},r.a.createElement(N.a,{src:a.preview,fit:"cover"})),r.a.createElement(x.a,{weight:"bold"},(t=a.name).length>15?t.substr(0,15)+"...":t),l&&r.a.createElement(x.a,null,A(a.size).value.toFixed(1)," ",A(a.size).suffix))};I.defaultProps={file:{preview:void 0}};var U=function(e){var t=e.accept,a=e.maxSize,l=e.minSize,o=e.multiple,i=e.onAddFiles,c=e.onDeleteFiles,s=e.showPreview,u=e.showFileSize,m=Object(n.useState)([]),h=Object(g.a)(m,2),f=h[0],p=h[1],v=Object(n.useState)(!1),b=Object(g.a)(v,2),E=b[0],j=b[1],O=Object(n.createRef)(),k=Object(n.useCallback)((function(e){E||(s&&e.map((function(e){return Object.assign(e,{preview:URL.createObjectURL(e)})})),p([].concat(Object(d.a)(f),Object(d.a)(e))),i&&i(e),!o&&0===f.length&&e.length>0&&j(!0))}),[E,s,f,i,o]),x=Object(w.a)({accept:t,maxSize:a,minSize:l,multiple:o,noClick:f.length,onDrop:k}),S=x.getRootProps,C=x.getInputProps,T=x.isDragActive,N=function(e){var t=Object(d.a)(f);t.splice(t.indexOf(e),1),p(t),c&&c(t),0===t.length&&j(!1)},P=f.map((function(e,t){return r.a.createElement(z,{file:e,key:t,removeFile:N,showPreview:s,showFileSize:u,margin:{bottom:t!==f.length-1?"xsmall":"none"}})}));return r.a.createElement(y,Object.assign({isDragActive:T,files:f,ref:O},S()),r.a.createElement("input",C()),f.length?P:void 0,!f.length&&(T?r.a.createElement(F,{multiple:o}):r.a.createElement(D,{multiple:o})))};U.defaultProps={accept:"",maxSize:void 0,minSize:void 0,multiple:!1,onAddFiles:void 0,onDeleteFiles:void 0,showPreview:!1,showFileSize:!1};var q=function(e){Object(s.a)(a,e);var t=Object(u.a)(a);function a(e){var n;return Object(i.a)(this,a),(n=t.call(this,e)).state={value:"no link yet"},n}return Object(c.a)(a,[{key:"render",value:function(){var e=this.state.value;return function(){var t={url:e},a="https://lmm2b8jjoe.execute-api.ap-southeast-2.amazonaws.com/scrape";fetch("https://cors-anywhere.herokuapp.com/"+a,{method:"POST",body:JSON.stringify(t),headers:{"Content-Type":"application/json"}}).then((function(e){return e.text()})).then((function(e){return console.log(e)})).catch((function(){return console.log("Can\u2019t access "+a+" response. ERROR")}))}(),1}}]),a}(r.a.Component),J=function(){var e=Object(n.useState)([]),t=Object(g.a)(e,2),a=t[0],l=t[1];return r.a.createElement(f.a,{width:"290px",gap:"0",onDrop:function(e){return e.preventDefault()}},r.a.createElement(p.a,{onSubmit:function(e){e.preventDefault();var t=document.getElementById("LinkURL").value;console.log(t);var n=new q;n.state.value=t,n.render(),function(e){var t=e.firstName,a=e.lastName,n=e.files,r=new FormData;n.forEach((function(e){r.append(e,n[e])})),r.append(t,t),r.append(a,a),fetch("https://my-website.com/api/file/upload",{method:"POST",body:r}).then((function(e){return e.json().then((function(t){return{status:e.status,statusText:e.statusText,json:t}}))})).then((function(e){var t=e.status,a=e.statusText,n=e.json;if(!(t>=400))return n;console.log("error:",t,a,n)})).catch((function(e){return console.log(e)}))}({files:a})}},r.a.createElement(v.a.Extend,{value:{formField:{border:{color:"none"},label:{margin:{bottom:"small"}},margin:{bottom:"medium"}}}},r.a.createElement(b.a,null,r.a.createElement("input",{type:"url",id:"LinkURL",className:"URL",placeholder:"URL"}),r.a.createElement("hr",null),r.a.createElement(U,{multiple:!0,showPreview:!0,showFileSize:!0,onAddFiles:function(e){l.apply(void 0,Object(d.a)(a).concat([e]))},onDeleteFiles:function(e){l(e)}}))),r.a.createElement(f.a,{align:"start",direction:"row",gap:"xsmall"},r.a.createElement(E.a,{type:"submit",label:"Submit",primary:!0}))))},M=function(e){Object(s.a)(a,e);var t=Object(u.a)(a);function a(){return Object(i.a)(this,a),t.apply(this,arguments)}return Object(c.a)(a,[{key:"render",value:function(){return r.a.createElement("div",{className:"size"},r.a.createElement("img",{className:"Logo",src:"./logo_large.png",alt:""}))}}]),a}(r.a.Component),W=function(e){Object(s.a)(a,e);var t=Object(u.a)(a);function a(){return Object(i.a)(this,a),t.apply(this,arguments)}return Object(c.a)(a,[{key:"render",value:function(){return r.a.createElement(h.a,null,r.a.createElement(J,null))}}]),a}(r.a.Component),G=function(e){Object(s.a)(a,e);var t=Object(u.a)(a);function a(){return Object(i.a)(this,a),t.apply(this,arguments)}return Object(c.a)(a,[{key:"render",value:function(){return r.a.createElement("div",{className:"appcontent"},r.a.createElement("div",{className:"block"},r.a.createElement(M,null),r.a.createElement("br",null),"Drag and drop an image to verify its authenticity."),r.a.createElement("hr",null),r.a.createElement("div",{className:"block"},r.a.createElement("div",{className:"flex-spacer"},r.a.createElement("p",null,"Reverse Image Search"),r.a.createElement(m.Toggle,{leftBackgroundColor:"#D1D1D1",rightBackgroundColor:"#663399",borderColor:"none",knobColor:"white",name:"toggle-1",onToggle:function(e){return console.log("onToggle1",e.target.checked)}})),r.a.createElement("hr",null)),r.a.createElement("div",{className:"block"},r.a.createElement("div",{className:"flex-spacer"},r.a.createElement("p",null,"Check digital image manipulation"),r.a.createElement(m.Toggle,{leftBackgroundColor:"#D1D1D1",rightBackgroundColor:"#663399",borderColor:"none",knobColor:"white",name:"toggle-2",onToggle:function(e){return console.log("onToggle2",e.target.checked)}})),r.a.createElement("hr",null)),r.a.createElement("div",{className:"block"},r.a.createElement("div",{className:"flex-spacer"},r.a.createElement("p",null,"Show in feed"),r.a.createElement(m.Toggle,{leftBackgroundColor:"#D1D1D1",rightBackgroundColor:"#663399",borderColor:"none",knobColor:"white",name:"toggle-3",onToggle:function(e){return console.log("onToggle3",e.target.checked)}}))),r.a.createElement("div",{className:"block dropper"},r.a.createElement(W,null)),r.a.createElement("hr",null),r.a.createElement("div",{className:"block italic"},r.a.createElement("p",null,"This image has been digitally manipulated and has a suspicious history, would you like to see the ",r.a.createElement("a",{href:"google.com"},"original?"))))}}]),a}(r.a.Component),K=G,$=document.getElementById("root");o.a.render(r.a.createElement(G,null),$);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(K,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[58,1,2]]]);