import urllib.parse
import os
import re

class Text:
    Green, Red, White, Yellow = '\033[92m', '\033[91m', '\033[97m', '\033[93m'
    Bold, Italics = '\033[1m', '\x1B[3m'
    Reset = '\033[0m'  # This turns off all attributes

def sanitize_filename(name: str) -> str:
    """Sanitize the filename to remove invalid characters."""
    name = name.strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', name)

def create_folder(path):
    os.makedirs(path, exist_ok=True)

def find_common_prefix(list_of_lists):
    """Finds the common prefix among a list of lists."""
    if not list_of_lists:
        return []
    common_prefix = list_of_lists[0]
    for lst in list_of_lists[1:]:
        i = 0
        while i < len(common_prefix) and i < len(lst) and common_prefix[i] == lst[i]:
            i += 1
        common_prefix = common_prefix[:i]
        if not common_prefix:
            break
    return common_prefix

def group_links_by_first_non_common_path_segment(links):
    """Groups links based on the first non-common path segment."""
    # Extract path segments for all links
    all_path_segments = []
    for link in links:
        parsed_url = urllib.parse.urlparse(link)
        path_segments = parsed_url.path.strip('/').split('/')
        all_path_segments.append(path_segments)

    # Find the common prefix among all path segments
    common_prefix = find_common_prefix(all_path_segments)

    grouped_links = {}
    for link, path_segments in zip(links, all_path_segments):
        # Remove common prefix
        remaining_segments = path_segments[len(common_prefix):]
        if remaining_segments:
            group = remaining_segments[0]
        else:
            group = 'root'
        if group not in grouped_links:
            grouped_links[group] = []
        grouped_links[group].append(link)
    return grouped_links
