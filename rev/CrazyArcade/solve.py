
MEM_SIZE = 0x25
MEM = [0x00] * MEM_SIZE

'''
MEM = [
0x7F, 0x19, 0x8A, 0xB7,
0xF0, 0x81, 0x2D, 0x54,
0xC9, 0xCA, 0xDD, 0xB8,
0x32, 0x23, 0xC3, 0xD3,
0x2E, 0xC9, 0x53, 0x02,
0xAB, 0x81, 0x41, 0xBA,
0xD2, 0x95, 0xED, 0xAB,
0xAD, 0x20, 0x7E, 0xD6,
0x92, 0x2A, 0xE7, 0xB6,
0x3E,
]
'''


MEM = [
	0xB7, 0x8A, 0x19, 0x7f,
	0x54, 0x2d, 0x81, 0xf0,
	0xb8, 0xdd, 0xca, 0xc9,
	0xd3, 0xc3, 0x23, 0x32,
	0xba, 0x41, 0x81, 0xab,
	0x02, 0x53, 0xc9, 0x2e,
	0xd6, 0x7e, 0x20, 0xad,
	0xab, 0xed, 0x95, 0xd2,
	0xb6, 0xe7, 0x2a, 0x92,
	0x3e
]


QWORD_SIZE = 0x584 # 1412
QWORD = [0] * QWORD_SIZE

QWORD = [

0x48, 0x89, 0x54, 0x24, 0x10, 0x53, 0x57, 0x48, 0x83, 0xEC, 0x48, 0x48, 0x8B, 0xFA, 0x33, 0xDB,
0x89, 0x5F, 0x30, 0x48, 0x89, 0x5F, 0x38, 0x48, 0x8B, 0x87, 0xB8, 0x00, 0x00, 0x00, 0x4C, 0x8B,
0x57, 0x18, 0x8B, 0x50, 0x10, 0x44, 0x8B, 0x48, 0x08, 0x80, 0x38, 0x0E, 0x0F, 0x85, 0x3B, 0x05,
0x00, 0x00, 0x8B, 0x40, 0x18, 0x05, 0x00, 0xE0, 0xFF, 0x7F, 0x83, 0xF8, 0x54, 0x0F, 0x87, 0x23,
0x05, 0x00, 0x00, 0x4C, 0x8D, 0x05, 0x86, 0x05, 0x00, 0x00, 0x49, 0x0F, 0xB6, 0x04, 0x00, 0x4C,
0x8D, 0x05, 0x2E, 0x05, 0x00, 0x00, 0x49, 0x63, 0x04, 0x80, 0x4C, 0x8D, 0x05, 0x05, 0x00, 0x00,
0x00, 0x49, 0x03, 0xC0, 0xFF, 0xE0, 0x83, 0xFA, 0x30, 0x75, 0x5F, 0x49, 0x8B, 0x4A, 0x08, 0x48,
0x85, 0xC9, 0x74, 0x4A, 0x41, 0x8B, 0x42, 0x18, 0x83, 0xE8, 0x01, 0x74, 0x25, 0x83, 0xE8, 0x01,
0x74, 0x12, 0x83, 0xE8, 0x02, 0x75, 0x27, 0x41, 0x8B, 0x42, 0x14, 0x8B, 0x04, 0x08, 0x41, 0x89,
0x42, 0x1C, 0xEB, 0x1A, 0x41, 0x8B, 0x42, 0x14, 0x0F, 0xB7, 0x04, 0x08, 0x41, 0x89, 0x42, 0x1C,
0xEB, 0x0C, 0x41, 0x8B, 0x42, 0x14, 0x0F, 0xB6, 0x04, 0x08, 0x41, 0x89, 0x42, 0x1C, 0x89, 0x5F,
0x30, 0x48, 0xC7, 0x47, 0x38, 0x30, 0x00, 0x00, 0x00, 0xE9, 0xAF, 0x04, 0x00, 0x00, 0xC7, 0x47,
0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0xA3, 0x04, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00,
0xC0, 0xE9, 0x97, 0x04, 0x00, 0x00, 0x83, 0xFA, 0x30, 0x75, 0x5F, 0x49, 0x8B, 0x52, 0x08, 0x48,
0x85, 0xD2, 0x74, 0x4A, 0x41, 0x8B, 0x42, 0x18, 0x83, 0xE8, 0x01, 0x74, 0x26, 0x83, 0xE8, 0x01,
0x74, 0x12, 0x83, 0xE8, 0x02, 0x75, 0x27, 0x41, 0x8B, 0x4A, 0x14, 0x41, 0x8B, 0x42, 0x1C, 0x89,
0x04, 0x11, 0xEB, 0x1A, 0x41, 0x8B, 0x4A, 0x14, 0x66, 0x41, 0x8B, 0x42, 0x1C, 0x66, 0x89, 0x04,
0x11, 0xEB, 0x0B, 0x41, 0x8B, 0x4A, 0x14, 0x41, 0x8A, 0x42, 0x1C, 0x88, 0x04, 0x11, 0x89, 0x5F,
0x30, 0x48, 0xC7, 0x47, 0x38, 0x30, 0x00, 0x00, 0x00, 0xE9, 0x3F, 0x04, 0x00, 0x00, 0xC7, 0x47,
0x30, 0x9A, 0x00, 0x00, 0xC0, 0xE9, 0x33, 0x04, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00,
0xC0, 0xE9, 0x27, 0x04, 0x00, 0x00, 0x83, 0xFA, 0x30, 0x75, 0x28, 0x49, 0x8B, 0xCA, 0xE8, 0xFD,
0xFD, 0xFF, 0xFF, 0x89, 0x47, 0x30, 0x85, 0xC0, 0x7C, 0x0D, 0x48, 0xC7, 0x47, 0x38, 0x30, 0x00,
0x00, 0x00, 0xE9, 0x06, 0x04, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x9A, 0x00, 0x00, 0xC0, 0xE9, 0xFA,
0x03, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0xEE, 0x03, 0x00, 0x00, 0x83,
0xFA, 0x30, 0x75, 0x27, 0x49, 0x8B, 0x4A, 0x08, 0x48, 0x85, 0xC9, 0x74, 0x12, 0x41, 0x8B, 0x52,
0x10, 0xFF, 0x15, 0x71, 0x0A, 0x00, 0x00, 0x89, 0x5F, 0x30, 0xE9, 0xCE, 0x03, 0x00, 0x00, 0xC7,
0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0xC2, 0x03, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00,
0x00, 0xC0, 0xE9, 0xB6, 0x03, 0x00, 0x00, 0x44, 0x8B, 0xC2, 0x49, 0x8B, 0xD2, 0xE8, 0x0E, 0xFB,
0xFF, 0xFF, 0x89, 0x47, 0x30, 0x85, 0xC0, 0x7C, 0x0E, 0xB8, 0x08, 0x00, 0x00, 0x00, 0x48, 0x89,
0x47, 0x38, 0xE9, 0x96, 0x03, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0x8A,
0x03, 0x00, 0x00, 0x83, 0xFA, 0x08, 0x72, 0x1B, 0x49, 0x8B, 0x12, 0x48, 0xB9, 0xFF, 0xFF, 0xFF,
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x15, 0x05, 0x0A, 0x00, 0x00, 0x89, 0x47, 0x30, 0xE9, 0x6A,
0x03, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x01, 0x00, 0x00, 0xC0, 0xE9, 0x5E, 0x03, 0x00, 0x00, 0x83,
0xFA, 0x08, 0x75, 0x1D, 0x66, 0x41, 0x8B, 0x12, 0xEC, 0x0F, 0xBE, 0xC0, 0x41, 0x89, 0x42, 0x04,
0x89, 0x5F, 0x30, 0xB8, 0x08, 0x00, 0x00, 0x00, 0x48, 0x89, 0x47, 0x38, 0xE9, 0x3C, 0x03, 0x00,
0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0x30, 0x03, 0x00, 0x00, 0x83, 0xFA, 0x08,
0x75, 0x1E, 0x66, 0x41, 0x8B, 0x12, 0x66, 0xED, 0x0F, 0xB7, 0xC0, 0x41, 0x89, 0x42, 0x04, 0x89,
0x5F, 0x30, 0xB8, 0x08, 0x00, 0x00, 0x00, 0x48, 0x89, 0x47, 0x38, 0xE9, 0x0D, 0x03, 0x00, 0x00,
0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0x01, 0x03, 0x00, 0x00, 0x83, 0xFA, 0x08, 0x75,
0x1A, 0x66, 0x41, 0x8B, 0x12, 0xED, 0x41, 0x89, 0x42, 0x04, 0x89, 0x5F, 0x30, 0xB8, 0x08, 0x00,
0x00, 0x00, 0x48, 0x89, 0x47, 0x38, 0xE9, 0xE2, 0x02, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00,
0x00, 0xC0, 0xE9, 0xD6, 0x02, 0x00, 0x00, 0x83, 0xFA, 0x08, 0x75, 0x36, 0x41, 0x8B, 0x52, 0x04,
0x41, 0x8B, 0x0A, 0xE8, 0x28, 0xFD, 0xFF, 0xFF, 0x84, 0xC0, 0x75, 0x0C, 0xC7, 0x47, 0x30, 0x0D,
0x00, 0x00, 0xC0, 0xE9, 0xB5, 0x02, 0x00, 0x00, 0x66, 0x41, 0x8B, 0x12, 0x41, 0x8A, 0x42, 0x04,
0xEE, 0x89, 0x5F, 0x30, 0xB8, 0x08, 0x00, 0x00, 0x00, 0x48, 0x89, 0x47, 0x38, 0xE9, 0x9B, 0x02,
0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0x8F, 0x02, 0x00, 0x00, 0x83, 0xFA,
0x08, 0x75, 0x38, 0x41, 0x8B, 0x52, 0x04, 0x41, 0x8B, 0x0A, 0xE8, 0xE1, 0xFC, 0xFF, 0xFF, 0x84,
0xC0, 0x75, 0x0C, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0x6E, 0x02, 0x00, 0x00, 0x66,
0x41, 0x8B, 0x12, 0x66, 0x41, 0x8B, 0x42, 0x04, 0x66, 0xEF, 0x89, 0x5F, 0x30, 0xB8, 0x08, 0x00,
0x00, 0x00, 0x48, 0x89, 0x47, 0x38, 0xE9, 0x52, 0x02, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00,
0x00, 0xC0, 0xE9, 0x46, 0x02, 0x00, 0x00, 0x83, 0xFA, 0x08, 0x75, 0x36, 0x41, 0x8B, 0x52, 0x04,
0x41, 0x8B, 0x0A, 0xE8, 0x98, 0xFC, 0xFF, 0xFF, 0x84, 0xC0, 0x75, 0x0C, 0xC7, 0x47, 0x30, 0x0D,
0x00, 0x00, 0xC0, 0xE9, 0x25, 0x02, 0x00, 0x00, 0x66, 0x41, 0x8B, 0x12, 0x41, 0x8B, 0x42, 0x04,
0xEF, 0x89, 0x5F, 0x30, 0xB8, 0x08, 0x00, 0x00, 0x00, 0x48, 0x89, 0x47, 0x38, 0xE9, 0x0B, 0x02,
0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0xFF, 0x01, 0x00, 0x00, 0x83, 0xFA,
0x08, 0x75, 0x1C, 0x41, 0xC7, 0x02, 0x01, 0x00, 0x00, 0x00, 0xB8, 0x08, 0x00, 0x00, 0x00, 0x41,
0x89, 0x42, 0x04, 0x89, 0x5F, 0x30, 0x48, 0x89, 0x47, 0x38, 0xE9, 0xDE, 0x01, 0x00, 0x00, 0xC7,
0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0xD2, 0x01, 0x00, 0x00, 0x83, 0xFA, 0x08, 0x75, 0x35,
0x41, 0x8B, 0x02, 0x8B, 0x0D, 0x5B, 0x18, 0x00, 0x00, 0x3D, 0x00, 0x00, 0x00, 0x80, 0x0F, 0x45,
0xC8, 0x89, 0x0D, 0x4D, 0x18, 0x00, 0x00, 0x41, 0x03, 0x4A, 0x04, 0x89, 0x0D, 0x43, 0x18, 0x00,
0x00, 0x41, 0x89, 0x0A, 0x89, 0x5F, 0x30, 0xB8, 0x08, 0x00, 0x00, 0x00, 0x48, 0x89, 0x47, 0x38,
0xE9, 0x98, 0x01, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0x8C, 0x01, 0x00,
0x00, 0x83, 0xFA, 0x0C, 0x75, 0x44, 0x41, 0x8B, 0x0A, 0x0F, 0x32, 0x8B, 0xCA, 0x48, 0xC1, 0xE1,
0x20, 0x48, 0x0B, 0xC8, 0x48, 0x89, 0x4C, 0x24, 0x30, 0x48, 0xC1, 0xE9, 0x20, 0x41, 0x89, 0x4A,
0x04, 0x8B, 0x44, 0x24, 0x30, 0x41, 0x89, 0x42, 0x08, 0x89, 0x5F, 0x30, 0x48, 0xC7, 0x47, 0x38,
0x0C, 0x00, 0x00, 0x00, 0xE9, 0x54, 0x01, 0x00, 0x00, 0x48, 0x8B, 0x7C, 0x24, 0x68, 0xC7, 0x47,
0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0x43, 0x01, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00,
0xC0, 0xE9, 0x37, 0x01, 0x00, 0x00, 0x83, 0xFA, 0x0C, 0x75, 0x3C, 0x41, 0x8B, 0x42, 0x04, 0x48,
0xC1, 0xE0, 0x20, 0x41, 0x8B, 0x4A, 0x08, 0x48, 0x0B, 0xC1, 0x48, 0x8B, 0xD0, 0x48, 0xC1, 0xEA,
0x20, 0x41, 0x8B, 0x0A, 0x0F, 0x30, 0x89, 0x5F, 0x30, 0x48, 0xC7, 0x47, 0x38, 0x0C, 0x00, 0x00,
0x00, 0xE9, 0x07, 0x01, 0x00, 0x00, 0x48, 0x8B, 0x7C, 0x24, 0x68, 0xC7, 0x47, 0x30, 0x0D, 0x00,
0x00, 0xC0, 0xE9, 0xF6, 0x00, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xE9, 0xEA,
0x00, 0x00, 0x00, 0x83, 0xFA, 0x18, 0x75, 0x5D, 0x41, 0x8B, 0x4A, 0x10, 0x85, 0xC9, 0x74, 0x49,
0x83, 0xF9, 0x04, 0x77, 0x44, 0x4D, 0x8D, 0x4A, 0x14, 0x45, 0x8B, 0x42, 0x08, 0x41, 0x83, 0xE0,
0x07, 0x41, 0xC1, 0xE0, 0x05, 0x41, 0x8B, 0x42, 0x04, 0x83, 0xE0, 0x1F, 0x44, 0x0B, 0xC0, 0x89,
0x4C, 0x24, 0x28, 0x41, 0x8B, 0x42, 0x0C, 0x89, 0x44, 0x24, 0x20, 0x41, 0x8B, 0x12, 0xB9, 0x04,
0x00, 0x00, 0x00, 0xFF, 0x15, 0xEF, 0x06, 0x00, 0x00, 0x89, 0x5F, 0x30, 0x48, 0xC7, 0x47, 0x38,
0x18, 0x00, 0x00, 0x00, 0xE9, 0x94, 0x00, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0,
0xE9, 0x88, 0x00, 0x00, 0x00, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xEB, 0x7F, 0x83, 0xFA,
0x18, 0x75, 0x6A, 0x41, 0x8B, 0x4A, 0x10, 0x85, 0xC9, 0x74, 0x59, 0x83, 0xF9, 0x04, 0x77, 0x54,
0x41, 0x8B, 0x52, 0x0C, 0x83, 0xFA, 0x10, 0x72, 0x0E, 0x83, 0xFA, 0x27, 0x77, 0x09, 0xC7, 0x47,
0x30, 0x0D, 0x00, 0x00, 0xC0, 0xEB, 0x56, 0x4D, 0x8D, 0x4A, 0x14, 0x45, 0x8B, 0x42, 0x08, 0x41,
0x83, 0xE0, 0x07, 0x41, 0xC1, 0xE0, 0x05, 0x41, 0x8B, 0x42, 0x04, 0x83, 0xE0, 0x1F, 0x44, 0x0B,
0xC0, 0x89, 0x4C, 0x24, 0x28, 0x89, 0x54, 0x24, 0x20, 0x41, 0x8B, 0x12, 0xB9, 0x04, 0x00, 0x00,
0x00, 0xFF, 0x15, 0x79, 0x06, 0x00, 0x00, 0x89, 0x5F, 0x30, 0x48, 0xC7, 0x47, 0x38, 0x18, 0x00,
0x00, 0x00, 0xEB, 0x19, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0xEB, 0x10, 0xC7, 0x47, 0x30,
0x0D, 0x00, 0x00, 0xC0, 0xEB, 0x07, 0xC7, 0x47, 0x30, 0x0D, 0x00, 0x00, 0xC0, 0x8B, 0x5F, 0x30,
0x32, 0xD2, 0x48, 0x8B, 0xCF, 0xFF, 0x15, 0xB5, 0x06, 0x00, 0x00, 0x8B, 0xC3, 0x48, 0x83, 0xC4,
0x48, 0x5F, 0x5B, 0xC3, 0x00, 0x00, 0x00, 0x00, 0xD5, 0x18, 0x9A, 0xE4, 0x98, 0xBD, 0x00, 0x10,

]


win = 0


while win < 0x1337:

	addr = win % MEM_SIZE # + DRIVER_ADDR + 0x3000

	read_value = MEM[addr]

	write_value = ((win ^ read_value) % 256) ^ QWORD[win % QWORD_SIZE]

	MEM[addr] = write_value 

	win += 1




print(MEM)

try:

	flag = ''.join([chr(char) for char in MEM])
	print(flag)

except Exception as e:
	print(e)


# hitcon{cr4zy_arc4de_wi7h_vuln_dr1ver}