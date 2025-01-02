import os
import polib

def compile_po_files():
    locale_dir = 'locale'
    for lang in ['ru', 'en', 'uz']:
        po_path = os.path.join(locale_dir, lang, 'LC_MESSAGES', 'django.po')
        mo_path = os.path.join(locale_dir, lang, 'LC_MESSAGES', 'django.mo')
        
        if os.path.exists(po_path):
            po = polib.pofile(po_path)
            po.save_as_mofile(mo_path)
            print(f"Compiled {po_path} to {mo_path}")

if __name__ == '__main__':
    compile_po_files()
