with open('styles.css', encoding='utf-8') as f:
    c = f.read()

# Replace the entire testimonial-track block speed + gap
c = c.replace(
    'animation: scroll-testimonials 20s linear infinite;',
    'animation: scroll-testimonials 10s linear infinite;'
)
c = c.replace(
    'animation-duration: 15s;',
    'animation-duration: 8s;'
)
c = c.replace(
    'animation-duration: 30s;',
    'animation-duration: 14s;'
)

# Remove margin-right from testimonial-card so truly no gap
c = c.replace('  margin-right: 1.5rem;\n', '')

# Also ensure gap stays 0 on track
c = c.replace('  gap: 0;\n  padding: 1rem 0;\n', '  gap: 0;\n  padding: 1rem 0;\n')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(c)

print("Done - speed 10s, no gap")
