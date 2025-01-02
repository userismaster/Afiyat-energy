from django import template

register = template.Library()

@register.filter(name='get_translated_name')
def get_translated_name(obj, language):
    """
    Get the translated name of an object based on the language
    """
    try:
        if language == 'en' and hasattr(obj, 'name_en') and obj.name_en:
            return obj.name_en
        elif language == 'uz' and hasattr(obj, 'name_uz') and obj.name_uz:
            return obj.name_uz
        return obj.name  # Default to Russian name
    except AttributeError:
        return str(obj)  # Fallback if no name attribute exists

@register.filter(name='get_translated_description')
def get_translated_description(obj, language):
    """
    Get the translated description of an object based on the language
    """
    try:
        if language == 'en' and hasattr(obj, 'description_en') and obj.description_en:
            return obj.description_en
        elif language == 'uz' and hasattr(obj, 'description_uz') and obj.description_uz:
            return obj.description_uz
        return obj.description  # Default to Russian description
    except AttributeError:
        return ''  # Fallback if no description attribute exists
