import math
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.944969, -0.226974, -0.23562)

# Set the basic save options.
save_atts = SaveWindowAttributes()
save_atts.family = 0
save_atts.format = save_atts.PNG
save_atts.resConstraint = save_atts.NoConstraint
save_atts.width = 1200
save_atts.height = 1068

# Get the number of time steps.
n_time_steps = TimeSliderGetNStates()

# Loop over the time states saving an image for each state.
for time_step in range(0,n_time_steps):
    TimeSliderSetState(time_step)
    angle = (time_step / n_time_steps * 1.0) * 2 * math.pi
    View3DAtts.viewNormal = (math.sin(angle), -0.226974, -0.23562)
    SetView3D(View3DAtts)
    save_atts.fileName = "AnMesh%04d.png" % time_step
    SetSaveWindowAttributes(save_atts)
    SaveWindow()