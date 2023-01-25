import bpy

import os

if __name__ == "__main__":
    
    ######## all you need to change #########

    outdir = '/Users/spock-the-wizard/Desktop/wonjong/siggraph/'
#    name = 'Figure10'
    name = 'Figure1'
    name = 'Figure7'
    #########################3
    
    collection = bpy.data.collections[name]
    outdir = os.path.join(outdir,collection.name)
    
    scn = bpy.context.scene
    # disable rendering for all objects
    for obj in scn.objects:
        if name == 'Figure1' and obj.name.startswith('Light'):
            obj.hide_render = False
            continue
        elif name != 'Figure1' and obj.name == 'Point':
            obj.hide_render = False
            continue
        obj.hide_render = True
        
    bpy.context.scene.render.film_transparent = True
    
    
    if name == 'Figure10':
        name_list = ['10_1','10_2']
        for name in name_list:
            obj = scn.objects[name]
            scn.objects[obj.name].hide_render = False
            fname = os.path.join(outdir,obj.name+'.png')
            
            bpy.context.scene.render.filepath = fname
            bpy.ops.render.render(write_still=True)
            print('saved %s'%fname)
           
            scn.objects[obj.name].hide_render = True
    elif name == 'Figure7':
        name_list = ['%d_%s'%(i,j) for j in ['toon','side_pix','side_sfs','side_style','deca','pix','deca_det','deep','sfs','style'] for i in range(1,5)]
#        name_list = [n for n in name_list if 'side' in n]
        for obj in scn.objects:
            if obj.name in name_list:
                print(obj.name)
                scn.objects[obj.name].hide_render = False
                fname = os.path.join(outdir,obj.name+'.png')
                
                bpy.context.scene.render.filepath = fname
                bpy.ops.render.render(write_still=True)
                print('saved %s'%fname)
                               
                scn.objects[obj.name].hide_render = True
    elif name == 'Figure1':
        
        name_list = ['1_%s_%s'%(i,j) for i in ['female','male'] for j in ['l','m','r']]
        for obj in scn.objects:
            if obj.name in name_list:
                print(obj.name)
                scn.objects[obj.name].hide_render = False
                fname = os.path.join(outdir,obj.name+'.png')
                
                bpy.context.scene.render.filepath = fname
                bpy.ops.render.render(write_still=True)
                print('saved %s'%fname)
               
                
                scn.objects[obj.name].hide_render = True