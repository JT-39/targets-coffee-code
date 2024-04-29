from graphviz import Source

gph_path = "src/data_analysis_gph/launch-code.dot"

gph1 = Source.from_file(gph_path)
gph1.render("_images/launch-code", format="png", view=False)