#version 430

in vec2 pass_texCoords;

out vec4 outColor;

uniform sampler2D textureSampler;

void
main() {
    outColor = texture(textureSampler, pass_texCoords);
    //outColor = vec4(0.384f, 0.506f, 0.192f, 0.1f);
    }

