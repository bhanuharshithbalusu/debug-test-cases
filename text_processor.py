
class SlidingWindowChunker:
    def __init__(self, chunk_size: int, overlap: int):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> list[str]:
        if not text:
            return []
            
        chunks = []
        start = 0
        
        while start < len(text):
            end = min(start + self.chunk_size, len(text))
            chunks.append(text[start:end])
            
            # BUG: The sliding window logic is wrong. 
            # It should move forward by (chunk_size - overlap).
            # Currently it just moves forward by chunk_size, resulting in 0 overlap.
            start += self.chunk_size 
            
            # Additional logic error: 
            # If start becomes equal to len(text) due to exactly matching chunk size, 
            # the loop might terminate correctly, but it doesn't handle the 
            # 'overlap' requirement for the next chunk's context.
            
        return chunks

if __name__ == "__main__":
    processor = SlidingWindowChunker(chunk_size=10, overlap=3)
    sample_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Expected: ["ABCDEFGHIJ", "HIJKLMNOPQ", "OPQRSTUVWX", "XYZ"] (with overlap)
    # Actual:   ["ABCDEFGHIJ", "KLMNOPQRST", "UVWXYZ"] (no overlap, missing context)
    result = processor.chunk(sample_text)
    print(f"Text length: {len(sample_text)}")
    print(f"Chunks: {result}")
