def interpret_blur(blur_score):
    if blur_score < 100:
        return True, "blurry"
    return False, None


def interpret_brightness(brightness):
    if brightness < 60:
        return True, "too_dark"
    elif brightness > 220:
        return True, "overexposed"
    return False, None


def interpret_edge_density(edge_density):
    if edge_density > 25:
        return True, "cluttered_background"
    return False, None


def compute_quality_score(is_blurry, brightness_issue, background_issue):
    score = 1.0

    if is_blurry:
        score -= 0.4
    if brightness_issue:
        score -= 0.2
    if background_issue:
        score -= 0.2

    return max(round(score, 2), 0.0)
