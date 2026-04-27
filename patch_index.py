import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('podcast_html.txt', 'r', encoding='utf-8') as f:
    new_grid = f.read()

# Find the start and end of the grid-3 div inside the podcast section
podcast_start = html.find('id="podcast"')
grid_start = html.find('<div class="grid-3">', podcast_start)
grid_end = html.find('</section>', grid_start)
grid_end = html.rfind('</div>', grid_start, grid_end) + 6 # end of grid-3 div

new_html = html[:grid_start] + new_grid + html[grid_end:]

# Add a modal for playing videos at the end of the body
modal_html = """
    <!-- Video Modal -->
    <div id="video-modal" class="modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9); z-index: 1000; align-items: center; justify-content: center; flex-direction: column;">
        <button id="close-modal" style="position: absolute; top: 2rem; right: 2rem; background: transparent; border: none; color: white; cursor: pointer;"><i data-lucide="x" style="width: 32px; height: 32px;"></i></button>
        <div style="width: 90%; max-width: 1000px; aspect-ratio: 16/9; background: #000;">
            <iframe id="video-iframe" src="" style="width: 100%; height: 100%; border: none;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
    </div>
"""

new_html = new_html.replace('</body>', modal_html + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
