from io import StringIO

from .keyvalues import KeyValues


class K3Vmdl:
    def __init__(self):
        self.storage = {'rootNode': {'_class': 'RootNode',
                                     'children': [],
                                     'model_archetype': '',
                                     'primary_associated_entity': '',
                                     'anim_graph_name': '',
                                     }}

        self.render_mesh_list = {'_class': 'RenderMeshList', 'children': []}

        self.animation_list = {'_class': 'AnimationList', 'children': []}

        self.bodygroup_list = {'_class': 'BodyGroupList', 'children': []}

        self.storage['rootNode']['children'].append(self.render_mesh_list)
        self.storage['rootNode']['children'].append(self.animation_list)
        self.storage['rootNode']['children'].append(self.bodygroup_list)
        self._add_empty_anim()

    # def add_anim(self):

    def _add_empty_anim(self):
        anim = {'_class': 'EmptyAnim',
                'activity_name': '',
                'activity_weight': 1,
                'anim_markup_ordered': False,
                'delta': False,
                'disable_compression': False,
                'fade_in_time': 0.2,
                'fade_out_time': 0.2,
                'frame_count': 1,
                'frame_rate': 30,
                'hidden': False,
                'looping': False,
                'name': 'ref',
                'weight_list_name': '',
                'worldSpace': False}
        self.animation_list['children'].append(anim)

    def add_render_mesh(self, name, path):
        render_mesh = {'_class': 'RenderMeshFile',
                       'name': name,
                       'filename': path,
                       'import_scale': 1.0
                       }

        self.render_mesh_list['children'].append(render_mesh)

    def add_bodygroup(self, name):
        bodygroup = {'_class': 'BodyGroup',
                     'children': [],
                     'hidden_in_tools': False,
                     'name': name}
        self.bodygroup_list['children'].append(bodygroup)
        return bodygroup

    @staticmethod
    def add_bodygroup_choice(bodygroup, meshes_name):
        if isinstance(meshes_name, str):
            meshes_name = [meshes_name]
        choice = {'_class': 'BodyGroupChoice', 'meshes': meshes_name}
        bodygroup['children'].append(choice)

    def dump(self):
        string = StringIO()
        KeyValues.dump(('KV3',
                        ('text', 'e21c7f3c-8a33-41c5-9977-a76d3a32aa0d'),
                        ('modeldoc28', 'fb63b6ca-f435-4aa0-a2c7-c66ddc651dca')),
                       self.storage, string)
        string.seek(0)
        return string.read(-1)
