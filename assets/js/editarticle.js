$(function() {
    $('#article_preview_btn').click(function() {
        var converter = new showdown.Converter();
        var content_html = converter.makeHtml($('#content').val());
        $('#article_preview').html(content_html);
    });
});