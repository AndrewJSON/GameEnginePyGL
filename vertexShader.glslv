#version 430 core

in vec3 vPosition;
in vec2 texCoords;

out vec2 pass_texCoords;

void
main() {
    gl_Position = vec4( vPosition, 1.0 );
    pass_texCoords = texCoords;
    }

