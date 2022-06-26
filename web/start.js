function initiate(){
    // python
    filename = document.getElementById('filename').value
    eel.gui(filename)(call_back)
}

function call_back(output) {
    $('#above_main').attr('class','container-fluid')
    $('#main').css('height','auto')
    $('#main').html('<pre>'+prettyPrintJson.toHtml(output)+'</pre>')
    // document.getElementById('above_main').className = 'container-fluid'
    // document.getElementById('main').style.height = 'auto'
    // document.getElementById('main').innerHTML = `<pre>${JSON.stringify(output,undefined,2)}</pre>`
}