#pragma once

/* Copyright © 2018-2019 MAKER.                                               */
/* This code is licensed under the MIT License.                               */
/* See: LICENSE.md                                                            */

#include <skift/generic.h>

void graphic_early_setup(uint width, uint height);
void graphic_setup();

void graphic_blit(uint *buffer);
void graphic_blit_region(uint *buffer, uint x, uint y, uint w, uint h);
void graphic_size(uint *width, uint *height);
void graphic_pixel(uint x, uint y, uint color);