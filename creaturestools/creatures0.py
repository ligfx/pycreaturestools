from PIL import Image
from PIL.ImagePalette import ImagePalette

from ._io_utils import *

# this is the palette from PALETTE.DTA
# note that Creatures 0 has five other palettes as well — 0.PAL through 4.PAL
CREATURES0_PALETTE = ImagePalette(
    palette=[
        # fmt: off
    0x00,0x00,0x00, 0x44,0x44,0xFC, 0x00,0xA8,0x00, 0xFC,0x00,0xA4, 0xFC,0x00,0xA4, 0xFC,0x00,0xA4,
    0xFC,0x00,0xA4, 0xFC,0x00,0xA4, 0xFC,0x00,0xA4, 0xFC,0x00,0xA4, 0xFC,0x00,0xA4, 0xFC,0x00,0xA4,
    0xFC,0x00,0xA4, 0xFC,0x00,0xA4, 0xFC,0x00,0xA4, 0xFC,0x00,0xA4, 0xA4,0xCC,0xD0, 0xA4,0xCC,0xD0,
    0x78,0xBC,0xD4, 0x50,0xA0,0xD8, 0xFC,0x00,0xA4, 0xFC,0x00,0xA4, 0xFC,0x00,0xA4, 0xFC,0x00,0xA4,
    0x28,0xAC,0xD0, 0x24,0xA0,0xC0, 0x20,0x90,0xB0, 0x20,0x84,0xA0, 0x1C,0x78,0x90, 0x18,0x68,0x7C,
    0x14,0x58,0x68, 0x10,0x48,0x54, 0x00,0xFC,0x00, 0x00,0xFC,0x00, 0x00,0xFC,0x00, 0x00,0xFC,0x00,
    0x00,0xFC,0x00, 0x00,0xFC,0x00, 0x00,0xFC,0x00, 0x00,0xFC,0x00, 0xFC,0x9C,0x00, 0xFC,0x88,0x00,
    0xFC,0x70,0x00, 0x40,0x78,0x84, 0x38,0x68,0x74, 0x2C,0x58,0x60, 0x24,0x44,0x4C, 0x1C,0x34,0x3C,
    0xD4,0xE8,0xEC, 0xBC,0xDC,0xE0, 0xA4,0xCC,0xD0, 0x90,0xC0,0xC4, 0x7C,0xB4,0xB8, 0x68,0xA8,0xAC,
    0x58,0x9C,0xA0, 0x48,0x90,0x94, 0x38,0x84,0x88, 0x2C,0x78,0x7C, 0x20,0x6C,0x70, 0x18,0x64,0x64,
    0x10,0x58,0x58, 0x08,0x4C,0x48, 0x04,0x3C,0x3C, 0x00,0x30,0x30, 0xE8,0xE4,0xDC, 0xE8,0xD0,0xC0,
    0xEC,0xC8,0xB0, 0xEC,0xC0,0xA4, 0xE0,0xB0,0xA0, 0xD4,0xA4,0x9C, 0xC8,0x98,0x98, 0xC0,0x94,0x98,
    0xB8,0x88,0x88, 0xA0,0x70,0x74, 0xE8,0x80,0x6C, 0xBC,0x68,0x60, 0xA4,0x5C,0x50, 0x90,0x54,0x48,
    0x88,0x4C,0x44, 0x80,0x44,0x40, 0x74,0x3C,0x3C, 0xD4,0x88,0x70, 0xCC,0x80,0x68, 0xC0,0x7C,0x60,
    0xBC,0x74,0x58, 0xB4,0x68,0x48, 0xB4,0x70,0x58, 0xAC,0x5C,0x34, 0xA8,0x5C,0x48, 0xAC,0x60,0x40,
    0xAC,0x6C,0x54, 0x90,0x5C,0x48, 0x78,0x48,0x40, 0x88,0x50,0x40, 0x98,0x58,0x40, 0xFC,0x00,0xFC,
    0xE4,0xC0,0xB0, 0xD8,0xB8,0xA8, 0xD4,0xAC,0x98, 0xD0,0xA0,0x88, 0xD4,0x9C,0x84, 0xDC,0x98,0x84,
    0xC8,0x8C,0x84, 0x98,0x6C,0x68, 0x7C,0x58,0x58, 0x88,0x48,0x4C, 0x90,0x4C,0x4C, 0x98,0x54,0x50,
    0xA4,0x5C,0x54, 0xAC,0x68,0x58, 0xE0,0xD0,0xD0, 0xD4,0xC0,0xC4, 0xC8,0xB4,0xB8, 0xBC,0xA8,0xB0,
    0xD4,0xD4,0xE4, 0xCC,0xC8,0xDC, 0xC4,0xC0,0xD4, 0xB8,0xC8,0xD0, 0xAC,0xBC,0xBC, 0x98,0xA8,0xA0,
    0x84,0x94,0x84, 0x78,0x80,0x74, 0x74,0x74,0x6C, 0x68,0x68,0x60, 0x5C,0x5C,0x54, 0x50,0x50,0x48,
    0x44,0x44,0x3C, 0x34,0x34,0x30, 0xF0,0x8C,0x5C, 0xE0,0x84,0x54, 0xD0,0x78,0x4C, 0xC4,0x68,0x40,
    0xBC,0x54,0x30, 0xB0,0x48,0x24, 0xA0,0x48,0x24, 0x94,0x44,0x24, 0x84,0x3C,0x20, 0x74,0x30,0x18,
    0x74,0x18,0x18, 0x88,0x60,0x64, 0x74,0x50,0x50, 0x74,0x48,0x48, 0x74,0x3C,0x3C, 0x74,0x3C,0x2C,
    0x74,0x44,0x18, 0x6C,0x3C,0x18, 0x5C,0x34,0x14, 0x4C,0x2C,0x10, 0xCC,0xD0,0xE8, 0xC0,0xC0,0xD8,
    0xB4,0xB8,0xCC, 0xAC,0xA8,0xBC, 0xA0,0x98,0xA8, 0x94,0x88,0x98, 0x88,0x7C,0x88, 0x74,0x6C,0x74,
    0x68,0x60,0x64, 0x5C,0x54,0x58, 0x50,0x48,0x4C, 0x40,0x3C,0x3C, 0x20,0x7C,0x70, 0x0C,0x60,0x64,
    0x04,0x48,0x4C, 0x00,0x30,0x30, 0x3C,0x94,0x7C, 0x34,0x84,0x6C, 0x2C,0x74,0x60, 0x38,0x70,0x54,
    0x40,0x6C,0x48, 0x44,0x64,0x44, 0x4C,0x60,0x40, 0x50,0x5C,0x38, 0xD8,0xD8,0xA0, 0xD8,0xD0,0x90,
    0xDC,0xC8,0x80, 0xB8,0xC8,0x70, 0xAC,0xC0,0x6C, 0x9C,0xB4,0x64, 0x8C,0xA8,0x5C, 0x80,0xA0,0x54,
    0x74,0x94,0x44, 0x68,0x8C,0x34, 0x5C,0x84,0x24, 0x6C,0x80,0x24, 0x74,0x78,0x24, 0x70,0x68,0x24,
    0x64,0x5C,0x2C, 0x54,0x50,0x30, 0xD8,0xD0,0x84, 0xD8,0xCC,0x6C, 0xD8,0xC4,0x54, 0xB4,0xA4,0x4C,
    0xFC,0xD8,0x8C, 0xFC,0xD8,0x74, 0xFC,0xD8,0x58, 0xFC,0xC4,0x50, 0xF4,0xB0,0x48, 0xE4,0xA8,0x44,
    0xD8,0xA4,0x3C, 0xD8,0x90,0x00, 0xE0,0x7C,0x00, 0xE8,0x6C,0x00, 0xF4,0x54,0x00, 0xFC,0x40,0x00,
    0xE8,0x34,0x1C, 0xD0,0x30,0x38, 0xC4,0x0C,0x54, 0xBC,0x2C,0x40, 0xFC,0xB4,0x64, 0xFC,0xA8,0x48,
    0xFC,0xAC,0x00, 0xD0,0x58,0x0C, 0xBC,0x3C,0x10, 0xAC,0x28,0x14, 0x9C,0x20,0x18, 0xF0,0x98,0x90,
    0xE0,0x78,0x78, 0xD0,0x68,0x70, 0xC0,0x54,0x68, 0xB0,0x44,0x5C, 0xA0,0x34,0x54, 0x90,0x28,0x50,
    0x80,0x1C,0x4C, 0x70,0x10,0x44, 0x64,0xA8,0xC0, 0x58,0x9C,0xB4, 0x48,0x8C,0xA4, 0x3C,0x80,0x98,
    0x38,0x78,0x98, 0x30,0x6C,0x9C, 0x38,0x64,0x94, 0x3C,0x60,0x88, 0x3C,0x58,0x80, 0x24,0x4C,0x78,
    0x10,0x3C,0x70, 0x00,0x34,0x64, 0x00,0x30,0x60, 0x8C,0x58,0x70, 0x84,0x40,0x60, 0x6C,0x60,0x7C,
    0x6C,0x4C,0x7C, 0x74,0x38,0x78, 0x74,0x24,0x64, 0x7C,0x28,0x50, 0xE8,0x88,0x74, 0xDC,0x74,0x64,
    0xCC,0x64,0x54, 0xC0,0x54,0x48, 0xB4,0x44,0x3C, 0xA4,0x38,0x30, 0x98,0x2C,0x28, 0x8C,0x20,0x20,
    0x80,0x50,0x70, 0x70,0x44,0x6C, 0x70,0x48,0x64, 0x6C,0x4C,0x5C
        # fmt: on
    ]
)

CREATURES0_SPRITE_BACKGROUND_PIECE_NAMES = ["{:03}.SPR".format(_) for _ in range(128)]


def read_creatures0_spr_file(fname_or_stream, palette=None):
    with open_if_not_stream(fname_or_stream, "rb") as f:
        num_images = read_u16le(f)
        next_offset = 2 + 4 * num_images
        widths = []
        heights = []
        for _ in range(num_images):
            offset = read_u16le(f)
            if offset != next_offset:
                raise Exception(
                    "Expected image offset to be {}, but got {}".format(
                        next_offset, offset
                    )
                )
            widths.append(read_u8(f))
            heights.append(read_u8(f))
            next_offset += widths[-1] * heights[-1]

        if (
            num_images == 16
            and all(_ == 80 for _ in widths)
            and all(_ == 40 for _ in heights)
        ):
            # this is a piece of a background! we don't have all the pieces, but we can at least stitch this one up
            # NOTE: this is _not_ stitched in the same way that other background files are.
            # we go row-by-row, instead of column by column.
            width_blocks = 4
            height_blocks = 4
            totalwidth = 320
            totalheight = 160

            data = bytearray(totalwidth * totalheight)
            for i in range(num_images):
                x = i % width_blocks
                y = i // width_blocks
                for blocky in range(40):
                    start = (y * 40 + blocky) * totalwidth + x * 80
                    data[start : start + 80] = read_exact(f, 80)

            image = Image.frombytes(
                "P",
                (totalwidth, totalheight),
                bytes(data),
            )
            image.putpalette(palette or CREATURES0_PALETTE)
            return [image]
        else:
            images = []
            for i in range(num_images):
                data = f.read(widths[i] * heights[i])
                img = Image.frombytes("P", size=(widths[i], heights[i]), data=data)
                img.putpalette(palette or CREATURES0_PALETTE)
                images.append(img)
            return images


def is_creatures0_sprite_file(fname_or_stream):
    with open_if_not_stream(fname_or_stream, "rb") as f:
        header = peek_exact(f, 6)
        num_images = struct.unpack("<H", header[0:2])[0]
        creatures1_spr_offset = struct.unpack("<I", header[2:6])[0]
        if creatures1_spr_offset >= 65536:
            # probably? this seems way too big, it would only happen if offset
            # is actually a 16-bit number
            return True
    return False


def is_creatures0_sprite_background_piece(images):
    return len(images) == 1 and images[0].width == 320 and images[0].height == 160


def stitch_creatures0_sprite_background(images):
    if len(images) != 128:
        raise Exception(
            "Expected number of images to be 128, but got {}".format(len(images))
        )
    for i in images:
        if not is_creatures0_sprite_background_piece([i]):
            raise Exception(
                "Expected image to be a creatures0 sprite background piece, but got {}".format(
                    i
                )
            )

    sprwidth = 320
    sprheight = 160
    heightinsprites = 4
    widthinsprites = 32
    totalwidth = sprwidth * widthinsprites
    totalheight = sprheight * heightinsprites

    newimage = Image.new("P", size=(totalwidth, totalheight))
    newimage.putpalette(images[0].getpalette())

    for i in range(heightinsprites):
        for j in range(widthinsprites):
            whereweare = j + i * widthinsprites
            newimage.paste(
                images[whereweare],
                (j * sprwidth, i * sprheight, (j + 1) * sprwidth, (i + 1) * sprheight),
            )
    return newimage
