$(function() {
    var converter = new showdown.Converter();
    var article_html = converter.makeHtml($('#article_content').val())
    $('#article_viewer').html(article_html)
});