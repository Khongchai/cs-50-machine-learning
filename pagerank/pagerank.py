import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


# This is the page rank equation
def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    pages = corpus.keys()
    distribution = {
        # initialize with random distribution
        page: (1 - damping_factor) / len(pages) for page in pages
    }

    direct_links = set(corpus[page])
    for link in direct_links:
        distribution[link] += damping_factor / len(direct_links)

    return distribution

def sample_pagerank(corpus: dict[str], damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    pages = corpus.keys()
    ranks = {
        p: 0 for p in pages
    }

    next = random.sample(sorted(pages), 1)[0]

    for _ in range(n):
        distribution = transition_model(corpus, next, damping_factor)
        for page in pages:
            ranks[page] += distribution[page]

        links = corpus[next]
        weights = [distribution[link] for link in links]
        next = random.choices(sorted(links), weights=weights, k=1)[0]

    for page in ranks:
        ranks[page] /= n

    return ranks

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = corpus.keys()
    
    page_ranks = dict()

    links_to = dict()
    for k, v in corpus.items():
        if links_to[v] is None:
            links_to[v] = set()
        links_to[v].add(k)

# todo not doing the subtracting (giving away) thing yet.
    diff = 1
    ep = sys.float_info.epsilon
    while(diff > ep):
        for p in pages:
            major_weight = 0
            for link in links_to[p]:
                major_weight += damping_factor * (page_ranks[link] / len(links_to[p]))

            minor_weight = ((1 - damping_factor) / len(pages)) 
            distribution = major_weight + minor_weight
            page_ranks[p] = distribution
            diff = max(distribution, diff)

    return page_ranks

if __name__ == "__main__":
    main()
