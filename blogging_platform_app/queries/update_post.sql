UPDATE posts
SET title = %s, content = %s, category = %s, tags = %s, updated_at = CURRENT_TIMESTAMP
WHERE id = %s;