from generate_latex_files import LatexTableRenderer
from generate_textual_model_rendering import TextualModelRenderer
from metamodels.guidance_metamodel import decision
from plant_uml_renderer import PlantUMLGenerator
from python.data_as_a_product_codeablemodels.data_as_a_product_models.data_as_a_product_model import data_as_a_product_views
# from data_as_a_product_models import domain_model_views

# UMLgenerator
generator = PlantUMLGenerator(delete_gen_dir_during_init=True)
generator.object_model_renderer.name_break_length = 45
generator.object_model_renderer.left_to_right = True

object_models = {'data_as_a_product': data_as_a_product_views}
for key, value in object_models.items():
    generator.generate_object_models(key, value)

# class_models = {'domain_model': domain_model_views}
# for key, value in class_models.items():
#     generator.generate_class_models(key, value)

# TextualInfo
textual_model_renderer = TextualModelRenderer()
decisions = [d for d in decision.all_classes]
textual_model_renderer.generate_guidance_evidences(decisions, "api_design")

# Latex
#source_table_renderer = LatexTableRenderer()
#source_table_renderer.generate(decisions)

#%%
