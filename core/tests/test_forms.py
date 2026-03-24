from django.test import TestCase

from core.forms import ContactForm


class ContactFormTest(TestCase):
    """
    Tests para el formulario de contacto.
    """

    # -------------------------------------------------------------------------
    # TEST 8: Formulario de contacto guarda correctamente
    # -------------------------------------------------------------------------
    def test_contact_form_saves_data(self):
        """
        Test: El formulario de contacto guarda datos válidos en la BD.
        """
        form_data = {
            "email": "visitante@example.com",
            "comentario": "Hola, me interesa tu trabajo, contáctame.",
        }

        form = ContactForm(data=form_data)

        self.assertTrue(form.is_valid(), f"Formulario inválido: {form.errors}")

        contact = form.save()

        self.assertEqual(contact.email, "visitante@example.com")
        self.assertEqual(
            contact.comentario, "Hola, me interesa tu trabajo, contáctame."
        )
        self.assertFalse(contact.contactado)
        from core.models import Contact

        contact_from_db = Contact.objects.get(id=contact.id)
        self.assertEqual(contact_from_db.email, "visitante@example.com")
