function onLoad(strLink) {
    hideTooltip();
    if (strLink) {
        document.getElementById("floatingURL").value = window.location.origin + "/" + strLink;
    }
}

function onPressInput() {
    let floatingURL = document.getElementById("floatingURL");
    floatingURL.select();
    document.execCommand("copy");
}

function showTooltip() {
    let floatingURL = document.getElementById("floatingURL");
    tooltip = bootstrap.Tooltip.getInstance(floatingURL);
    if (!tooltip) {
        tooltip = new bootstrap.Tooltip(floatingURL);
    }
    if (floatingURL.value) {
        console.log(floatingURL.value);
        tooltip.enable();
        tooltip.show();
    }
    let timer = setTimeout(hideTooltip, 500)
}

function hideTooltip() {
    let floatingURL = document.getElementById("floatingURL");
    tooltip = bootstrap.Tooltip.getInstance(floatingURL);
    if (!tooltip) {
        tooltip = new bootstrap.Tooltip(floatingURL);
    }
    tooltip.disable();
    tooltip.hide();
}