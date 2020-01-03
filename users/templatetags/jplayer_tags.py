from django import template
register = template.Library()

@register.filter
def render_jplayer(context, player):
    return {'player': player}
register.inclusion_tag('base_block/player.html', takes_context=True)(render_jplayer)
