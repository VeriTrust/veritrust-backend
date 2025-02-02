# Default route
async def root():
    return {"message": "Welcome to the VeriTrust Backend"}

# Health check route
async def health_check():
    return {"status": "ok"}