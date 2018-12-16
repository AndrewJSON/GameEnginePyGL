
vertex_shader = """
#version 400 core
in vec4 position;
void main()
{
   gl_Position = position;
}
"""

fragment_shader = """
#version 400 core
void main()
{
   gl_FragColor = vec4(0.384f, 0.506f, 0.192f, 1.0f);
}
"""

''' END '''

