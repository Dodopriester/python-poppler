# poppler-python: python binding to the poppler-cpp pdf lib
# Copyright (C) 2020, Charles Brunet <charles@cbrunet.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from poppler.pagerenderer import PageRenderer
from poppler.image import Image


def test_can_render():
    assert PageRenderer.can_render() is True


def test_image_format():
    renderer = PageRenderer()

    assert renderer.image_format == Image.Format.argb32


def test_set_image_format():
    renderer = PageRenderer()
    renderer.image_format = Image.Format.mono

    assert renderer.image_format == Image.Format.mono


def test_line_mode():
    renderer = PageRenderer()

    assert renderer.line_mode == PageRenderer.LineMode.default


def test_set_line_mode():
    renderer = PageRenderer()
    renderer.line_mode = PageRenderer.LineMode.solid

    assert renderer.line_mode == PageRenderer.LineMode.solid


def test_paper_color():
    renderer = PageRenderer()

    assert renderer.paper_color == 0xFFFFFFFF


def test_set_paper_color():
    renderer = PageRenderer()
    renderer.paper_color = 0x12345678

    assert renderer.paper_color == 0x12345678


def test_render_hints():
    renderer = PageRenderer()

    assert renderer.render_hints == 0


def test_set_render_hints():
    renderer = PageRenderer()
    renderer.render_hints = (
        PageRenderer.RenderHint.antialiasing
        | PageRenderer.RenderHint.text_antialiasing
        | PageRenderer.RenderHint.text_hinting
    )

    assert renderer.render_hints == 7


def test_set_render_hint():
    renderer = PageRenderer()
    renderer.render_hints = 7
    renderer.set_render_hint(PageRenderer.RenderHint.antialiasing, False)

    assert renderer.render_hints == 6


def test_render_page(pdf_page):
    renderer = PageRenderer()
    image = renderer.render_page(pdf_page)

    assert image.height == 792
    assert image.width == 612


def test_image_with_paper_color(pdf_page):
    renderer = PageRenderer()
    renderer.paper_color = 0xFF336699
    image = renderer.render_page(pdf_page)

    assert image.data[0:4] == b"\x99\x66\x33\xFF"